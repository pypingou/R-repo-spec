%global packname  flowViz
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          Visualization for flow cytometry

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-flowCore R-lattice 
Requires:         R-Biobase R-flowCore R-graphics R-grDevices R-grid R-KernSmooth R-lattice R-latticeExtra R-MASS R-methods R-RColorBrewer R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-flowCore R-lattice
BuildRequires:    R-Biobase R-flowCore R-graphics R-grDevices R-grid R-KernSmooth R-lattice R-latticeExtra R-MASS R-methods R-RColorBrewer R-stats R-utils 


%description
Provides visualization tools for flow cytometry data.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora