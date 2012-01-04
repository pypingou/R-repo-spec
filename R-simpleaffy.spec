%global packname  simpleaffy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.30.0
Release:          1%{?dist}
Summary:          Very simple high level analysis of Affymetrix data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-genefilter R-Biobase R-methods R-utils R-gcrma 

BuildRequires:    R-devel tex(latex) R-affy R-genefilter R-Biobase R-methods R-utils R-gcrma 

%description
Provides high level functions for reading Affy .CEL files, phenotypic
data, and then computing simple things with it, such as t-tests, fold
changes and the like. Makes heavy use of the affy library. Also has some
basic scatter plot functions and mechanisms for generating high resolution
journal figures...

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.30.0-1
- initial package for Fedora