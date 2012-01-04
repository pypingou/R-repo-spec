%global packname  frmaExampleData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.2
Release:          1%{?dist}
Summary:          Frma Example Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data files used by the examples in frma and frmaTools packages

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
%doc %{rlibdir}/frmaExampleData/DESCRIPTION
%doc %{rlibdir}/frmaExampleData/html
%{rlibdir}/frmaExampleData/NAMESPACE
%{rlibdir}/frmaExampleData/Meta
%{rlibdir}/frmaExampleData/data
%{rlibdir}/frmaExampleData/help
%{rlibdir}/frmaExampleData/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.2-1
- initial package for Fedora