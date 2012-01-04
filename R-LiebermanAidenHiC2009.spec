%global packname  LiebermanAidenHiC2009
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.10
Release:          1%{?dist}
Summary:          Selected data from the HiC paper of E. Lieberman-Aiden et al. in Science (2009)

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-KernSmooth R-IRanges 

BuildRequires:    R-devel tex(latex) R-KernSmooth R-IRanges 

%description
This package provides data that were presented in the article
"Comprehensive mapping of long-range interactions reveals folding
principles of the human genome", Science 2009 Oct 9;326(5950):289-93.
PMID: 19815776

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
%doc %{rlibdir}/LiebermanAidenHiC2009/html
%doc %{rlibdir}/LiebermanAidenHiC2009/DESCRIPTION
%doc %{rlibdir}/LiebermanAidenHiC2009/doc
%{rlibdir}/LiebermanAidenHiC2009/extdata
%{rlibdir}/LiebermanAidenHiC2009/Meta
%{rlibdir}/LiebermanAidenHiC2009/help
%{rlibdir}/LiebermanAidenHiC2009/data
%{rlibdir}/LiebermanAidenHiC2009/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.10-1
- initial package for Fedora