%global packname  Deducer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Deducer

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-ggplot2 R-JGR R-car R-multcomp R-effects R-foreign 

BuildRequires:    R-devel tex(latex) R-rJava R-ggplot2 R-JGR R-car R-multcomp R-effects R-foreign 

%description
An intuitive, cross-platform graphical data analysis system. It uses menus
and dialogs to guide the user efficiently through the data manipulation
and analysis process, and has an excel like spreadsheet for easy data
frame visualization and editing. Deducer works best when used with the
Java based R GUI JGR, but the dialogs can be called from the command line.
Dialogs have also been integrated into the Windows Rgui.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora