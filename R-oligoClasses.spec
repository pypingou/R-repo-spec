%global packname  oligoClasses
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          Classes for high-throughput arrays supported by oligo and crlmm

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase R-methods 
Requires:         R-graphics R-Biostrings R-affyio R-IRanges 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods
BuildRequires:    R-graphics R-Biostrings R-affyio R-IRanges 


%description
This package contains class definitions, validity checks, and
initialization methods for classes used by the oligo and crlmm packages.

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
%doc %{rlibdir}/oligoClasses/doc
%doc %{rlibdir}/oligoClasses/DESCRIPTION
%doc %{rlibdir}/oligoClasses/html
%{rlibdir}/oligoClasses/data
%{rlibdir}/oligoClasses/NAMESPACE
%{rlibdir}/oligoClasses/help
%{rlibdir}/oligoClasses/NEWS.Rd
%{rlibdir}/oligoClasses/INDEX
%{rlibdir}/oligoClasses/R
%{rlibdir}/oligoClasses/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora