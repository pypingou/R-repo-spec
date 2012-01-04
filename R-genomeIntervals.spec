%global packname  genomeIntervals
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Operations on genomic intervals

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-intervals 
Requires:         R-methods R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods R-intervals
BuildRequires:    R-methods R-Biobase 


%description
 This package defines classes for representing genomic intervals and
provides functions and methods for working with these. Note: The package
provides the basic infrastructure for and is enhanced by the package

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
%doc %{rlibdir}/genomeIntervals/html
%doc %{rlibdir}/genomeIntervals/doc
%doc %{rlibdir}/genomeIntervals/DESCRIPTION
%{rlibdir}/genomeIntervals/R
%{rlibdir}/genomeIntervals/help
%{rlibdir}/genomeIntervals/INDEX
%{rlibdir}/genomeIntervals/NAMESPACE
%{rlibdir}/genomeIntervals/example_files
%{rlibdir}/genomeIntervals/data
RPM build errors:
%{rlibdir}/genomeIntervals/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora