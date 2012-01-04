%global packname  flowQ
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.1
Release:          1%{?dist}
Summary:          Quality control for flow cytometry

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-outliers R-lattice R-flowViz R-methods R-mvoutlier R-bioDist R-parody R-RColorBrewer R-latticeExtra 

BuildRequires:    R-devel tex(latex) R-outliers R-lattice R-flowViz R-methods R-mvoutlier R-bioDist R-parody R-RColorBrewer R-latticeExtra 

%description
Provides quality control and quality assessment tools for flow cytometry

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.1-1
- initial package for Fedora