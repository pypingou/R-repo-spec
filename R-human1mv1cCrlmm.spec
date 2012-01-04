%global packname  human1mv1cCrlmm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
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
Package with metadata fast genotyping Illumina 1M arrays using the 'crlmm'

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
%doc %{rlibdir}/human1mv1cCrlmm/html
%doc %{rlibdir}/human1mv1cCrlmm/DESCRIPTION
%{rlibdir}/human1mv1cCrlmm/INDEX
%{rlibdir}/human1mv1cCrlmm/help
%{rlibdir}/human1mv1cCrlmm/NAMESPACE
%{rlibdir}/human1mv1cCrlmm/R
%{rlibdir}/human1mv1cCrlmm/extdata
%{rlibdir}/human1mv1cCrlmm/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora