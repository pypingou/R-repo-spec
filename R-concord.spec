%global packname  concord
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.9
Release:          1%{?dist}
Summary:          Concordance and reliability

Group:            Applications/Engineering 
License:          GPL Version 2 or later.
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Measures of concordance and reliability

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
%doc %{rlibdir}/concord/html
%doc %{rlibdir}/concord/DESCRIPTION
%{rlibdir}/concord/NAMESPACE
%{rlibdir}/concord/Meta
%{rlibdir}/concord/INDEX
%{rlibdir}/concord/R
%{rlibdir}/concord/help
%{rlibdir}/concord/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.9-1
- initial package for Fedora