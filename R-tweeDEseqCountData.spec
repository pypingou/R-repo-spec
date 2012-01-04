%global packname  tweeDEseqCountData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          RNA-seq count data employed in the vignette of the tweeDEseq package

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
RNA-seq count data from Pickrell et al. (2010) employed to illustrate the
use of the Poisson-Tweedie family of distributions with the tweeDEseq

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
%doc %{rlibdir}/tweeDEseqCountData/html
%doc %{rlibdir}/tweeDEseqCountData/DESCRIPTION
%{rlibdir}/tweeDEseqCountData/Meta
%{rlibdir}/tweeDEseqCountData/NAMESPACE
%{rlibdir}/tweeDEseqCountData/R
%{rlibdir}/tweeDEseqCountData/INDEX
%{rlibdir}/tweeDEseqCountData/help
%{rlibdir}/tweeDEseqCountData/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora