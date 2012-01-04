%global packname  dyad
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Analysis of dyadic observational data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Contains original implementation of the Gottman-Murray marriage model and
revisions using threshold autoregressive models. These programs allow
modeling of dyadic observational data, such as interaction between husband
and wife. Intended for researchers interested in modeling social behavior.

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
%doc %{rlibdir}/dyad/html
%doc %{rlibdir}/dyad/DESCRIPTION
%{rlibdir}/dyad/help
%{rlibdir}/dyad/INDEX
%{rlibdir}/dyad/Meta
%{rlibdir}/dyad/data
%{rlibdir}/dyad/R
%{rlibdir}/dyad/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora