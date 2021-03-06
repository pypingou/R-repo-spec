%global packname  PAnnBuilder
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          Protein annotation data package builder

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-RSQLite R-Biobase R-AnnotationDbi 
Requires:         R-methods R-utils R-Biobase R-DBI R-RSQLite R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-RSQLite R-Biobase R-AnnotationDbi
BuildRequires:    R-methods R-utils R-Biobase R-DBI R-RSQLite R-AnnotationDbi 


%description
Processing annotation data from public data repositories and building
protein-centric annotation data packages.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora