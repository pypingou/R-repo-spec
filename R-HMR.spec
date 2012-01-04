%global packname  HMR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Flux estimation with static chamber data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Statistical analysis of static chamber concentration data for trace gas
flux estimation

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
%doc %{rlibdir}/HMR/html
%doc %{rlibdir}/HMR/DESCRIPTION
%{rlibdir}/HMR/INDEX
%{rlibdir}/HMR/help
%{rlibdir}/HMR/Meta
%{rlibdir}/HMR/R
%{rlibdir}/HMR/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora