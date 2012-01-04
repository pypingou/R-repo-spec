%global packname  maCorrPlot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Visualize artificial correlation in microarray data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Graphically displays correlation in microarray data that is due to
insufficient normalization

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
%doc %{rlibdir}/maCorrPlot/doc
%doc %{rlibdir}/maCorrPlot/DESCRIPTION
%doc %{rlibdir}/maCorrPlot/html
%{rlibdir}/maCorrPlot/data
%{rlibdir}/maCorrPlot/R
%{rlibdir}/maCorrPlot/Meta
%{rlibdir}/maCorrPlot/NAMESPACE
%{rlibdir}/maCorrPlot/help
%{rlibdir}/maCorrPlot/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora