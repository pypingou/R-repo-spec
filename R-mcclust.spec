%global packname  mcclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Process an MCMC Sample of Clusterings

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lpSolve 


BuildRequires:    R-devel tex(latex) R-lpSolve



%description
Implements methods for processing a sample of (hard) clusterings, e.g. the
MCMC output of a Bayesian clustering model. Among them are methods that
find a single best clustering to represent the sample, which are based on
the posterior similarity matrix or a relabelling algorithm.

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
%doc %{rlibdir}/mcclust/DESCRIPTION
%doc %{rlibdir}/mcclust/html
%{rlibdir}/mcclust/NAMESPACE
%{rlibdir}/mcclust/Meta
%{rlibdir}/mcclust/R
%{rlibdir}/mcclust/libs
%{rlibdir}/mcclust/data
%{rlibdir}/mcclust/INDEX
%{rlibdir}/mcclust/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora