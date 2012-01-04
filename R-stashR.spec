%global packname  stashR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          A Set of Tools for Administering SHared Repositories

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-filehash 
Requires:         R-tools R-digest 

BuildRequires:    R-devel tex(latex) R-methods R-filehash
BuildRequires:    R-tools R-digest 


%description
A Set of Tools for Administering SHared Repositories

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
%doc %{rlibdir}/stashR/html
%doc %{rlibdir}/stashR/COPYING
%doc %{rlibdir}/stashR/DESCRIPTION
%{rlibdir}/stashR/NAMESPACE
%{rlibdir}/stashR/help
%{rlibdir}/stashR/R
%{rlibdir}/stashR/INDEX
%{rlibdir}/stashR/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.4-1
- initial package for Fedora