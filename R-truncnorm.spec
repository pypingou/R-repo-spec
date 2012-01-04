%global packname  truncnorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Truncated normal distribution

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
r/d/p/q functions for the truncated normal distribution

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
%doc %{rlibdir}/truncnorm/DESCRIPTION
%doc %{rlibdir}/truncnorm/html
%{rlibdir}/truncnorm/unittests
%{rlibdir}/truncnorm/libs
%{rlibdir}/truncnorm/help
%{rlibdir}/truncnorm/NAMESPACE
%{rlibdir}/truncnorm/Meta
%{rlibdir}/truncnorm/R
%{rlibdir}/truncnorm/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora