%global packname  AnnotationDbi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.10
Release:          1%{?dist}
Summary:          Annotation Database Interface

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-Biobase 
Requires:         R-methods R-utils R-Biobase R-DBI R-RSQLite R-IRanges 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-Biobase
BuildRequires:    R-methods R-utils R-Biobase R-DBI R-RSQLite R-IRanges 


%description
Provides user interface and database connection code for annotation data
packages using SQLite data storage.

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
%doc %{rlibdir}/AnnotationDbi/DESCRIPTION
%doc %{rlibdir}/AnnotationDbi/doc
%doc %{rlibdir}/AnnotationDbi/html
%doc %{rlibdir}/AnnotationDbi/NEWS
%{rlibdir}/AnnotationDbi/unitTests
%{rlibdir}/AnnotationDbi/AnnDbPkg-templates
%{rlibdir}/AnnotationDbi/Meta
%{rlibdir}/AnnotationDbi/ProbePkg-template
%{rlibdir}/AnnotationDbi/DBschemas
%{rlibdir}/AnnotationDbi/TODO
%{rlibdir}/AnnotationDbi/INDEX
RPM build errors:
%{rlibdir}/AnnotationDbi/NAMESPACE
%{rlibdir}/AnnotationDbi/NOTES-Herve
%{rlibdir}/AnnotationDbi/extdata
%{rlibdir}/AnnotationDbi/R
%{rlibdir}/AnnotationDbi/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.10-1
- initial package for Fedora