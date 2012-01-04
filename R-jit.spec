%global packname  jit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Just-in-time compiler for the R language

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Enable just-in-time (JIT) compilation. The functions in this package are
useful only under Ra and have no effect under R. See

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
%doc %{rlibdir}/jit/NEWS
%doc %{rlibdir}/jit/DESCRIPTION
%doc %{rlibdir}/jit/html
%{rlibdir}/jit/Meta
%{rlibdir}/jit/NAMESPACE
%{rlibdir}/jit/INDEX
%{rlibdir}/jit/R
%{rlibdir}/jit/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora