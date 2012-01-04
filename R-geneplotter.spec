%global packname  geneplotter
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.1
Release:          1%{?dist}
Summary:          Graphics related functions for Bioconductor

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-annotate R-lattice 
Requires:         R-annotate R-AnnotationDbi R-Biobase R-graphics R-grDevices R-grid R-methods R-RColorBrewer R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-Biobase R-annotate R-lattice
BuildRequires:    R-annotate R-AnnotationDbi R-Biobase R-graphics R-grDevices R-grid R-methods R-RColorBrewer R-stats R-utils 


%description
Some basic functions for plotting genetic data

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.1-1
- initial package for Fedora