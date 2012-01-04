%global packname  conf.design
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          Construction of factorial designs

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This small library contains a series of simple tools for constructing and
manipulating confounded and fractional factorial designs.

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
%doc %{rlibdir}/conf.design/DESCRIPTION
%doc %{rlibdir}/conf.design/doc
%doc %{rlibdir}/conf.design/html
%{rlibdir}/conf.design/Meta
%{rlibdir}/conf.design/LICENSE
%{rlibdir}/conf.design/R
%{rlibdir}/conf.design/NAMESPACE
%{rlibdir}/conf.design/help
%{rlibdir}/conf.design/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora