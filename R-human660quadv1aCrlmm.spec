%global packname  human660quadv1aCrlmm
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
Package with metadata for genotyping Illumina 660kQuad arrays using the
'crlmm' package.

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
%doc %{rlibdir}/human660quadv1aCrlmm/DESCRIPTION
%doc %{rlibdir}/human660quadv1aCrlmm/html
%{rlibdir}/human660quadv1aCrlmm/INDEX
%{rlibdir}/human660quadv1aCrlmm/Meta
%{rlibdir}/human660quadv1aCrlmm/NAMESPACE
%{rlibdir}/human660quadv1aCrlmm/extdata
%{rlibdir}/human660quadv1aCrlmm/R
%{rlibdir}/human660quadv1aCrlmm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora