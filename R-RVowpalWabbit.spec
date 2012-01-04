%global packname  RVowpalWabbit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          R interface to the Vowpal Wabbit

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp 


BuildRequires:    R-devel tex(latex) R-Rcpp



%description
R interface to Vowpal Wabbit fast out-of-core learning system The Vowpal
Wabbit (VW) project is a fast out-of-core learning system sponsored by
Yahoo! Research and written by John Langford along with a number of
contributors. . There are two ways to have a fast learning algorithm: (a)
start with a slow algorithm and speed it up, or (b) build an intrinsically
fast learning algorithm. This project is about approach (b), and it has
reached a state where it may be useful to others as a platform for
research and experimentation. . There are several optimization algorithms
available with the baseline being sparse gradient descent (GD) on a loss
function (several are available). The code should be easily usable. Its
only external dependence is on the Boost library, which is often installed
by default. . This R package does not include the distributed computing
implementation of the cluster/ directory of the upstream sources.  Use of
the software as a network servie is also not directly supported as the aim
is a simpler direct call from R for validation and comparison.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4-1
- initial package for Fedora