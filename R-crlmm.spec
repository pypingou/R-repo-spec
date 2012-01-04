%global packname  crlmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.1
Release:          1%{?dist}
Summary:          Genotype Calling (CRLMM) and Copy Number Analysis tool for Affymetrix SNP 5.0 and 6.0 and Illumina arrays.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-oligoClasses 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-oligoClasses 

%description
Faster implementation of CRLMM specific to SNP 5.0 and 6.0 arrays, as well
as a copy number tool specific to 5.0, 6.0, and Illumina platforms

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.1-1
- initial package for Fedora