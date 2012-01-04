%global packname  breastCancerNKI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Genexpression dataset published by van't Veer et al. [2002] and van de Vijver et al. [2002] (NKI).

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Genexpression data from a breast cancer study published by van't Veer et
al. in 2002 and van de Vijver et al. in 2002, provided as an eSet.

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
%doc %{rlibdir}/breastCancerNKI/html
%doc %{rlibdir}/breastCancerNKI/DESCRIPTION
%{rlibdir}/breastCancerNKI/help
%{rlibdir}/breastCancerNKI/data
%{rlibdir}/breastCancerNKI/Meta
%{rlibdir}/breastCancerNKI/INDEX
%{rlibdir}/breastCancerNKI/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora