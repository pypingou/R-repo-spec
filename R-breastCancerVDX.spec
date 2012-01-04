%global packname  breastCancerVDX
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Gene expression datasets published by Wang et al. [2005] and Minn et al. [2007] (VDX).

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Gene expression data from a breast cancer study published by Wang et al.
in 2005 and Minn et al. in 2007, provided as an eSet.

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
%doc %{rlibdir}/breastCancerVDX/DESCRIPTION
%doc %{rlibdir}/breastCancerVDX/html
%{rlibdir}/breastCancerVDX/help
%{rlibdir}/breastCancerVDX/data
%{rlibdir}/breastCancerVDX/Meta
%{rlibdir}/breastCancerVDX/INDEX
%{rlibdir}/breastCancerVDX/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora