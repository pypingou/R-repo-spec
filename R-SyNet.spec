%global packname  SyNet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Inference and Analysis of Sympatry Networks

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tkrplot R-tcltk 

BuildRequires:    R-devel tex(latex) R-tkrplot R-tcltk 

%description
Infers sympatry matrices from distributional data and analyzes them in
order to identify groups of species cohesively connected.

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
%doc %{rlibdir}/SyNet/DESCRIPTION
%doc %{rlibdir}/SyNet/html
%{rlibdir}/SyNet/help
%{rlibdir}/SyNet/Meta
%{rlibdir}/SyNet/data
%{rlibdir}/SyNet/R
%{rlibdir}/SyNet/NAMESPACE
%{rlibdir}/SyNet/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora