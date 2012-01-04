%global packname  estout
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1.1
Release:          1%{?dist}
Summary:          Estimates Output

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package is intended to speedup the process of creating
model-comparing tables common in Macroeconomics. The function collection
stores the estimates of several models and formats it to a table of the
form estimate starred and std.err. below. The default output is LaTeX but
output to CSV for later editing in a spreadsheet tool is possible as well.
It works for linear models (lm) and panel models from the "plm"-package
(plm). Two further implemented functions "descsto" and "desctab" enable
you to export descriptive statistics of data-frames and single variables
to LaTeX and CSV.

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
%doc %{rlibdir}/estout/html
%doc %{rlibdir}/estout/DESCRIPTION
%{rlibdir}/estout/R
%{rlibdir}/estout/Meta
%{rlibdir}/estout/help
%{rlibdir}/estout/INDEX
%{rlibdir}/estout/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1.1-1
- initial package for Fedora