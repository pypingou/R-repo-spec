%global packname  evd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.4
Release:          1%{?dist}
Summary:          Functions for extreme value distributions

Group:            Applications/Engineering 
License:          GPL (Version 2 or above)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Extends simulation, distribution, quantile and density functions to
univariate and multivariate parametric extreme value distributions, and
provides fitting functions which calculate maximum likelihood estimates
for univariate and bivariate maxima models, and for univariate and
bivariate threshold models.

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
%doc %{rlibdir}/evd/DESCRIPTION
%doc %{rlibdir}/evd/doc
%doc %{rlibdir}/evd/html
%doc %{rlibdir}/evd/CITATION
%{rlibdir}/evd/help
%{rlibdir}/evd/demos.txt
%{rlibdir}/evd/R
%{rlibdir}/evd/CHANGES
%{rlibdir}/evd/INDEX
%{rlibdir}/evd/NAMESPACE
%{rlibdir}/evd/demo
%{rlibdir}/evd/data
%{rlibdir}/evd/libs
%{rlibdir}/evd/README
%{rlibdir}/evd/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.4-1
- initial package for Fedora