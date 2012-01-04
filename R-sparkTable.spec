%global packname  sparkTable
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Sparklines and graphical tables for tex and html

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-xtable R-utils R-grid R-Cairo R-methods R-Rglpk R-StatMatch R-gridExtra R-RGraphics R-ggplot2 R-pixmap 

BuildRequires:    R-devel tex(latex) R-graphics R-xtable R-utils R-grid R-Cairo R-methods R-Rglpk R-StatMatch R-gridExtra R-RGraphics R-ggplot2 R-pixmap 

%description
Create Sparklines and graphical tables for documents and websites

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora