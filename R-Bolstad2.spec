%global packname  Bolstad2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.26
Release:          1%{?dist}
Summary:          Bolstad functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-26.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A set of R functions and data sets for the book Understanding
Computational Bayesian Statistics, Bolstad, W.M. (2009), John Wiley & Sons
ISBN 978-0470046098

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
%doc %{rlibdir}/Bolstad2/html
%doc %{rlibdir}/Bolstad2/DESCRIPTION
%{rlibdir}/Bolstad2/demo
%{rlibdir}/Bolstad2/NAMESPACE
%{rlibdir}/Bolstad2/help
%{rlibdir}/Bolstad2/INDEX
%{rlibdir}/Bolstad2/data
%{rlibdir}/Bolstad2/R
%{rlibdir}/Bolstad2/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.26-1
- initial package for Fedora