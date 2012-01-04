%global packname  RTOMO
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Visualization for seismic tomography

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-GEOmap R-RSEIS 

BuildRequires:    R-devel tex(latex) R-GEOmap R-RSEIS 

%description
Created mainly for use with seismic tomography, this program plots
tomographic images, and allows one to interact and query three-dimensional
tomographic models.  Vertical cross-sectional cuts can be extracted by
mouse click. Geographic information can be added easily.

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
%doc %{rlibdir}/RTOMO/html
%doc %{rlibdir}/RTOMO/DESCRIPTION
%{rlibdir}/RTOMO/demo
%{rlibdir}/RTOMO/NAMESPACE
%{rlibdir}/RTOMO/data
%{rlibdir}/RTOMO/R
%{rlibdir}/RTOMO/Meta
%{rlibdir}/RTOMO/help
%{rlibdir}/RTOMO/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora