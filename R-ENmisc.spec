%global packname  ENmisc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Neuwirth miscellaenous

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-vcd R-gWidgets R-gWidgetstcltk R-RColorBrewer 


BuildRequires:    R-devel tex(latex) R-Hmisc R-vcd R-gWidgets R-gWidgetstcltk R-RColorBrewer



%description
The ENmisc library contains utility function for different purposes:
mtapply and mlapply (multivariate version of tapply and lapply),
wtd.boxplot (a boxplot with weights), and a visual interface to
restructuring mosaic plots.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.3-1
- initial package for Fedora