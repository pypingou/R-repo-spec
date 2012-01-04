%global packname  tkrplot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.22
Release:          1%{?dist}
Summary:          TK Rplot

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-22.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices R-tcltk 

BuildRequires:    R-devel tex(latex) R-grDevices R-tcltk 

%description
simple mechanism for placing R graphics in a Tk widget

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
%doc %{rlibdir}/tkrplot/DESCRIPTION
%doc %{rlibdir}/tkrplot/html
%{rlibdir}/tkrplot/R
%{rlibdir}/tkrplot/libs
%{rlibdir}/tkrplot/NAMESPACE
%{rlibdir}/tkrplot/INDEX
%{rlibdir}/tkrplot/Meta
%{rlibdir}/tkrplot/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.22-1
- initial package for Fedora