%global packname  tripEstimation
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.37
Release:          1%{?dist}
Summary:          Metropolis sampler and supporting functions for estimating animal movement from archival tags and satellite fixes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-37.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-akima R-lattice R-mgcv R-rgdal R-sp R-zoo 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-akima R-lattice R-mgcv R-rgdal R-sp R-zoo 


%description
Data handling and estimation functions for animal movement estimation by
light level and satellite data. Image summaries from MCMC simulations of
point data, binned by time interval. Various convenience functions for
creating generic summary images for periods defined by the location
estimation and combining those in arbitrarily specified ways.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.37-1
- initial package for Fedora