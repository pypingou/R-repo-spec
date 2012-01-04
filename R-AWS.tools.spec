%global packname  AWS.tools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          R package to use Amazon Web Services

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
R package for Amazon Web Services EC2/S3

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
%doc %{rlibdir}/AWS.tools/DESCRIPTION
%doc %{rlibdir}/AWS.tools/html
%{rlibdir}/AWS.tools/R
%{rlibdir}/AWS.tools/INDEX
%{rlibdir}/AWS.tools/Meta
%{rlibdir}/AWS.tools/NAMESPACE
%{rlibdir}/AWS.tools/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora