%global packname  genomewidesnp5Crlmm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Metadata for fast genotyping with the 'crlmm' package

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Package with metadata for fast genotyping Affymetrix GenomeWideSnp_5
arrays using the 'crlmm' package. Annotation build is hg19.

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
%doc %{rlibdir}/genomewidesnp5Crlmm/DESCRIPTION
%doc %{rlibdir}/genomewidesnp5Crlmm/html
%{rlibdir}/genomewidesnp5Crlmm/extdata
%{rlibdir}/genomewidesnp5Crlmm/Meta
%{rlibdir}/genomewidesnp5Crlmm/help
%{rlibdir}/genomewidesnp5Crlmm/R
%{rlibdir}/genomewidesnp5Crlmm/INDEX
%{rlibdir}/genomewidesnp5Crlmm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora