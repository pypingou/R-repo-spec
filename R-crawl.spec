%global packname  crawl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Fit continuous-time correlated random walk models for animal movement data

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-sp 


BuildRequires:    R-devel tex(latex) R-mvtnorm R-sp



%description
The (C)orrelated (RA)ndom (W)alk (L)ibrary of R functions was designed for
fitting continuous-time correlated random walk (CTCRW) models with time
indexed covariates. The model is fit using the Kalman-Filter on a state
space version of the continuous-time stochastic movement process.

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
%doc %{rlibdir}/crawl/DESCRIPTION
%doc %{rlibdir}/crawl/html
%{rlibdir}/crawl/help
%{rlibdir}/crawl/Meta
%{rlibdir}/crawl/data
%{rlibdir}/crawl/R
%{rlibdir}/crawl/libs
%{rlibdir}/crawl/NAMESPACE
%{rlibdir}/crawl/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.2-1
- initial package for Fedora