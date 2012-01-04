%global packname  traitr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11
Release:          1%{?dist}
Summary:          An interface for creating GUIs modeled in part after traits UI module for python.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-digest R-proto R-gWidgets 


BuildRequires:    R-devel tex(latex) R-digest R-proto R-gWidgets



%description
An interface for creating GUIs modeled in part after the traits UI module
for python. The basic design takes advantage of the model-view-controller
design pattern. The interface makes basic dialogs quite easy to produce.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11-1
- initial package for Fedora