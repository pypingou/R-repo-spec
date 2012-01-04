%global packname  log10
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0.03
Release:          1%{?dist}
Summary:          Decimal log plotting in two and three dimensions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1.0-03.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Provides a range of function for 10-log plotting

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
%doc %{rlibdir}/log10/html
%doc %{rlibdir}/log10/DESCRIPTION
%{rlibdir}/log10/help
%{rlibdir}/log10/NAMESPACE
%{rlibdir}/log10/R
%{rlibdir}/log10/INDEX
%{rlibdir}/log10/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0.03-1
- initial package for Fedora