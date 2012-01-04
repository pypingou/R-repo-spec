%global packname  corcounts
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Generate correlated count random variables

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Generate high-dimensional correlated count random variables with a
prespecified Pearson correlation.

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
%doc %{rlibdir}/corcounts/DESCRIPTION
%doc %{rlibdir}/corcounts/html
%{rlibdir}/corcounts/INDEX
%{rlibdir}/corcounts/NAMESPACE
%{rlibdir}/corcounts/help
%{rlibdir}/corcounts/R
%{rlibdir}/corcounts/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora