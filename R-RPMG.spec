%global packname  RPMG
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.8
Release:          1%{?dist}
Summary:          Graphical User Interface (GUI) for interactive R analysis sessions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Poor Man's Gui: create interactive R analysis sessions

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
%doc %{rlibdir}/RPMG/html
%doc %{rlibdir}/RPMG/DESCRIPTION
%{rlibdir}/RPMG/R
%{rlibdir}/RPMG/help
%{rlibdir}/RPMG/INDEX
%{rlibdir}/RPMG/demo
%{rlibdir}/RPMG/NAMESPACE
%{rlibdir}/RPMG/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.8-1
- initial package for Fedora