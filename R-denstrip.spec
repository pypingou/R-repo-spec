%global packname  denstrip
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Density strips and other methods for compactly illustrating distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Graphical methods for compactly illustrating probability distributions,
including density strips, density regions, sectioned density plots and
varying width strips.

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
%doc %{rlibdir}/denstrip/DESCRIPTION
%doc %{rlibdir}/denstrip/html
%doc %{rlibdir}/denstrip/CITATION
%doc %{rlibdir}/denstrip/NEWS
%{rlibdir}/denstrip/NAMESPACE
%{rlibdir}/denstrip/help
%{rlibdir}/denstrip/Meta
%{rlibdir}/denstrip/INDEX
%{rlibdir}/denstrip/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.1-1
- initial package for Fedora