%global packname  HilbertVis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Hilbert curve visualization

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grid R-lattice 

BuildRequires:    R-devel tex(latex) R-grid R-lattice 

%description
Functions to visualize long vectors of integer data by means of Hilbert

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
%doc %{rlibdir}/HilbertVis/html
%doc %{rlibdir}/HilbertVis/DESCRIPTION
%doc %{rlibdir}/HilbertVis/doc
%doc %{rlibdir}/HilbertVis/CITATION
%{rlibdir}/HilbertVis/help
%{rlibdir}/HilbertVis/libs
%{rlibdir}/HilbertVis/NAMESPACE
%{rlibdir}/HilbertVis/R
%{rlibdir}/HilbertVis/Meta
%{rlibdir}/HilbertVis/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora