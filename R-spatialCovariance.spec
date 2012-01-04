%global packname  spatialCovariance
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.6
Release:          1%{?dist}
Summary:          Computation of spatial covariance matrices for data on rectangles

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions that compute the spatial covariance matrix for the matern and
power classes of spatial models, for data that arise on rectangular units.
 This code can also be used for the change of support problem and for
spatial data that arise on irregularly shaped regions like counties or
zipcodes by laying a fine grid of rectangles and aggregating the integrals
in a form of Riemann integration.

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
%doc %{rlibdir}/spatialCovariance/DESCRIPTION
%doc %{rlibdir}/spatialCovariance/html
%{rlibdir}/spatialCovariance/Meta
%{rlibdir}/spatialCovariance/NAMESPACE
%{rlibdir}/spatialCovariance/help
%{rlibdir}/spatialCovariance/INDEX
%{rlibdir}/spatialCovariance/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.6-1
- initial package for Fedora