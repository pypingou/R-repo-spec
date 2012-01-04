%global packname  edtdbg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Integrating R's debug() with Your Text Editor

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Integrates R's debugging facilities with your text editor, featuring code
tracking, variable display, quick breakpoint setting, and easy toggling of
function debug status.

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
%doc %{rlibdir}/edtdbg/DESCRIPTION
%doc %{rlibdir}/edtdbg/html
%{rlibdir}/edtdbg/INDEX
%{rlibdir}/edtdbg/help
%{rlibdir}/edtdbg/r_dbg.vim
%{rlibdir}/edtdbg/README
%{rlibdir}/edtdbg/Meta
%{rlibdir}/edtdbg/NAMESPACE
%{rlibdir}/edtdbg/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora