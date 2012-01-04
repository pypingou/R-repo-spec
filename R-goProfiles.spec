%global packname  goProfiles
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          goProfiles: an R package for the statistical analysis of functional profiles

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-AnnotationDbi R-GO.db 


BuildRequires:    R-devel tex(latex) R-Biobase R-AnnotationDbi R-GO.db



%description
The package implements methods to compare lists of genes based on
comparing the corresponding 'functional profiles'.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora