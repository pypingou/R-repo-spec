%global packname  pcurve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          Principal curve analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mgcv R-vegan R-MASS R-stats 


BuildRequires:    R-devel tex(latex) R-mgcv R-vegan R-MASS R-stats



%description
Fits a principal curve to a numeric multivariate dataset in arbitrary
dimensions. Produces diagnostic plots.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.3-1
- initial package for Fedora