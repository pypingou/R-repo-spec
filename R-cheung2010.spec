%global packname  cheung2010
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.21
Release:          1%{?dist}
Summary:          resources for genetics of gene expression based on Cheung et al 2010

Group:            Applications/Engineering 
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-GGtools R-GenomicRanges R-hgfocus.db 

BuildRequires:    R-devel tex(latex) R-Biobase R-GGtools R-GenomicRanges R-hgfocus.db 

%description
Data resources related to the PLoS Biology paper Polymorphic Cis- and
Trans-Regulation of Human Gene Expression, including small-footprint
smlSet support for 147 hgfocus arrays and corresponding HapMap genotypes
at 1.3 million SNP

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.21-1
- initial package for Fedora