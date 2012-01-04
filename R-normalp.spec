%global packname  normalp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.8
Release:          1%{?dist}
Summary:          Package for exponential power distributions (EPD)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of utilities refered to exponential power distributions, also
known as General Error Distribution

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
%doc %{rlibdir}/normalp/DESCRIPTION
%doc %{rlibdir}/normalp/html
%{rlibdir}/normalp/help
%{rlibdir}/normalp/Meta
%{rlibdir}/normalp/R
%{rlibdir}/normalp/INDEX
%{rlibdir}/normalp/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.8-1
- initial package for Fedora