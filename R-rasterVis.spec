%global packname  rasterVis
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.10.6
Release:          1%{?dist}
Summary:          Visualization methods for the raster package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.10-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-raster R-lattice R-latticeExtra R-hexbin 
Requires:         R-grid R-grDevices R-sp R-zoo R-RColorBrewer 

BuildRequires:    R-devel tex(latex) R-methods R-raster R-lattice R-latticeExtra R-hexbin
BuildRequires:    R-grid R-grDevices R-sp R-zoo R-RColorBrewer 


%description
The raster package defines classes and methods for spatial raster data
access and manipulation. The rasterVis package complements raster
providing a set of methods for enhanced visualization and interaction.

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
%doc %{rlibdir}/rasterVis/DESCRIPTION
%doc %{rlibdir}/rasterVis/html
%{rlibdir}/rasterVis/INDEX
%{rlibdir}/rasterVis/Meta
%{rlibdir}/rasterVis/R
%{rlibdir}/rasterVis/help
%{rlibdir}/rasterVis/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10.6-1
- initial package for Fedora