%global packname  twiddler
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Interactive manipulation of R expressions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Twiddler is an interactive tool that automatically creates a Tcl/Tk GUI
for manipulating variables in any R expression. See the documentation of
the function twiddle to get started.

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
%doc %{rlibdir}/twiddler/html
%doc %{rlibdir}/twiddler/DESCRIPTION
%{rlibdir}/twiddler/R
%{rlibdir}/twiddler/NAMESPACE
%{rlibdir}/twiddler/help
%{rlibdir}/twiddler/INDEX
%{rlibdir}/twiddler/Meta
%{rlibdir}/twiddler/unittests

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora