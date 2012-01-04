%global packname  FFD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Freedom From Disease

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics R-tcltk R-tkrplot R-R2HTML 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-tcltk R-tkrplot R-R2HTML 

%description
Functions, S4 classes/methods and a graphical user interface (GUI) to
design surveys to substantiate freedom from disease using a modified
hypergeometric function (see Cameron and Baldock, 1997). Herd
sensitivities are computed according to sampling strategies "individual
sampling" or "limited sampling" (see M. Ziller, T. Selhorst, J. Teuffert,
M. Kramer and H. Schlueter, 2002). Methods to compute the a-posteriori
alpha-error are implemented. Risk-based targeted sampling is supported.

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
%doc %{rlibdir}/FFD/DESCRIPTION
%doc %{rlibdir}/FFD/doc
%doc %{rlibdir}/FFD/html
%{rlibdir}/FFD/Meta
%{rlibdir}/FFD/libs
%{rlibdir}/FFD/help
%{rlibdir}/FFD/sheepData.csv
%{rlibdir}/FFD/GUI_Logo.ppm
%{rlibdir}/FFD/data
%{rlibdir}/FFD/GUI_Logo4.ppm
%{rlibdir}/FFD/R
%{rlibdir}/FFD/NAMESPACE
%{rlibdir}/FFD/GUI_Logo2.ppm
%{rlibdir}/FFD/INDEX
%{rlibdir}/FFD/GUI_Logo3.ppm

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora